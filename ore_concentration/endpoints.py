from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse

from jwt_auth.auth import get_current_user
from users.schemas import User
from .models import Mine, OreConcentration
from .schemas import MineSc, ConcentrationNote, DateRange, ResponseMines, ResponseConcentrationNote, CreateData


# Создаем общий роутер для эндпоинтов, связанных с записями о концентрации руд
ore_router = APIRouter()


# Эндпоинт для создания новых Шахт
# Эндпоинт закрыт от неавторизованных пользователей
@ore_router.post('/create_mine', response_model=CreateData)
def create_mine(mine: MineSc, current_user: User = Depends(get_current_user)):
    # Проверяем не занято ли название Шахты
    if Mine.objects.filter(name=mine.name).exists():
        raise HTTPException(status_code=400, detail=f"Mine with such name {mine.name} already exists!")

    try:
        # Если название не занято - пытаемся создать и сохранить новую Шахту
        # Клиент в ответ получит сообщение об успешной операции и ID записи в базе данных
        new_mine = Mine()
        new_mine.name = mine.name
        new_mine.save()
        return JSONResponse(status_code=200, content={"status": "success", "id": new_mine.id, "success": True})
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"Error - {err}")


# Эндпоинт для создания новых записей о концентрации руд
# Эндпоинт закрыт от неавторизованных пользователей
@ore_router.post('/create_ore_concentration_note', response_model=CreateData)
def create_ore_concentration_note(note: ConcentrationNote, current_user: User = Depends(get_current_user)):
    # Проверяем существует ли Шахта с названием, указанным пользователем
    if not Mine.objects.filter(name=note.mine_name).exists():
        raise HTTPException(status_code=400, detail=f"Mine with such name '{note.mine_name}' does not exist!")
    # Если шахта существует, получаем ее из базы данных
    mine = Mine.objects.get(name=note.mine_name)

    # В нашем случае на одну дату можно создать только одну запись о концентрации руд
    # Проверяем нет ли в базе данных уже созданной записи дял указанной шахты и на указанную дату
    if OreConcentration.objects.filter(concentration_date=note.concentration_date, mine_name=mine).exists():
        raise HTTPException(status_code=400, detail=f"There already created note for this date {note.concentration_date} and this Mine {note.mine_name}")

    try:
        # Если все проверки прошли хорошо, пытаемся создать новую запись о концентрации руд и сохранить ее в базу данных
        new_concentration_note = OreConcentration()

        new_concentration_note.mine_name = mine
        new_concentration_note.iron_concentration = note.iron_concentration
        new_concentration_note.silicon_concentration = note.silicon_concentration
        new_concentration_note.aluminum_concentration = note.aluminum_concentration
        new_concentration_note.calcium_concentration = note.calcium_concentration
        new_concentration_note.sulfur_concentration = note.sulfur_concentration
        new_concentration_note.concentration_date = note.concentration_date

        new_concentration_note.save()

        # Возвращаем пользователю сообщение об успешном завершении операции и ID записи в базе данных
        return JSONResponse(status_code=200, content={
            "status": "success",
            "id": new_concentration_note.id,
            "success": True
        })
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"Error - {err}")


# Эндпоинт для получения всех Шахт из базы данных
# Эндпоинт закрыт от неавторизованных пользователей
@ore_router.get('/get_mines', response_model=ResponseMines)
def get_all_mines(current_user: User = Depends(get_current_user)):
    mines = Mine.objects.all()

    if not mines:
        raise HTTPException(status_code=400, detail=f"There no mines created yet")
    res = []
    for mine in mines:
        res.append(mine.name)
    return JSONResponse(status_code=200, content={"status": "success", "mines": res})


# Эндпоинт для получения записей о концентрации руд за указанных промежуток времени (От - До)
# Эндпоинт закрыт от неавторизованных пользователей
# Хоть этот эндпоинт нацелен исключительно на получение данных (GET), в его теле передаются параметры для
# фильтрации данных. Стандарт HTTP не любит когда у GET запроса есть тело
# Поэтому было принято решение сделать этот эндпоинт в формате POST
# Для избегания ненужных конфликтов с стандартом HTTP
@ore_router.post('/get_ore_concentration_note', response_model=ResponseConcentrationNote)
def get_ore_concentration_note(date_range: DateRange, current_user: User = Depends(get_current_user)):
    # Получаем записи из базы данных в указанном диапазоне дат
    notes = OreConcentration.objects.filter(concentration_date__range=(date_range.start_date, date_range.end_date))
    # если записей в указанном диапазоне нет, выбрасываем HTTP исключение (ошибку)
    if not notes:
        raise HTTPException(status_code=400, detail=f"There no notes on this date range")
    res = []
    # Формируем JSON с полученными записями
    for note in notes:
        res.append(
            {
                'mine name': note.mine_name.name,
                'iron concentration': note.iron_concentration,
                'silicon concentration': note.silicon_concentration,
                'aluminum concentration': note.aluminum_concentration,
                'calcium concentration': note.calcium_concentration,
                'sulfur concentration': note.sulfur_concentration,
                'concentration date': str(note.concentration_date),
            }
        )
    # Возвращаем пользователю ответ об успешном завершении операции и с полученными записями в формате JSON
    return JSONResponse(status_code=200, content={"status": "success", "notes": res})

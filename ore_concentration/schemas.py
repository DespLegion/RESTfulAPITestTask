from datetime import date

from pydantic import BaseModel, constr, Field


# Модель Pydantic для валидации поступающих данных при создании новой Шахты
class MineSc(BaseModel):
    name: constr(max_length=54)


# Модель Pydantic для валидации поступающих данных при создании новой записи о концентрации руд
class ConcentrationNote(BaseModel):
    mine_name: constr(max_length=54)
    iron_concentration: float = Field(gt=0, le=99.9)
    silicon_concentration: float = Field(gt=0, le=99.9)
    aluminum_concentration: float = Field(gt=0, le=99.9)
    calcium_concentration: float = Field(gt=0, le=99.9)
    sulfur_concentration: float = Field(gt=0, le=99.9)
    concentration_date: date


# Модель Pydantic для валидации поступающих данных диапазона дат
class DateRange(BaseModel):
    start_date: date
    end_date: date


# Универсальная модель Pydantic для жесткого определения формата ответа
# сервера при успешном добавлении данных в базу данных
# (создание Шахты, создание записи о концентрации)
class CreateData(BaseModel):
    status: str
    id: int
    success: bool


# Модель Pydantic для жесткого определения формата ответа сервера
# при запросе на получение всех Шахт
class ResponseMines(BaseModel):
    status: str
    mines: list


# Модель Pydantic для жесткого определения формата ответа сервера
# при запросе на получение записей о концентрации руд
# Эту модель можно было сделать еще более строгой, при помощи дополнительной модели Pydantic
# строго определяющей формат списка notes, но было принято решение, что это излишне
class ResponseConcentrationNote(BaseModel):
    status: str
    notes: list

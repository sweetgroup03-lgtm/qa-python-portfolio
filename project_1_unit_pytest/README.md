# Project 1: Unit Tests with Pytest

## Stack

- Python
- pytest

## What this project demonstrates

- Basic test design
- Parametrized tests
- Fixtures
- Positive and negative checks

## What I tested

- `calculator.add`: корректность сложения для целых, отрицательных и дробных чисел
- `calculator.divide`: корректное деление и ошибка при делении на ноль
- `cart.total`: подсчет общей суммы добавленных позиций
- `cart.apply_discount`: расчет итоговой суммы со скидкой 0%, 10% и 100%
- `cart.add_price`: ошибка при попытке добавить отрицательную цену

## Run

```powershell
cd project_1_unit_pytest
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -v
```

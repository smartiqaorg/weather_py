from behave import *
from lesson_5.calc import Calc


@given('a calculator')
def step_impl(context):
    context.calculator = Calc()


@when('first number is {num}')
def step_impl(context, num):
    context.calculator.a = int(num)


@when('second number is {num}')
def step_impl(context, num):
    context.calculator.b = int(num)


@then('the sum of the numbers is {sum}')
def step_impl(context, sum):
    assert(context.calculator.add() == int(sum))


@then('the subtraction of the numbers is {sub}')
def step_impl(context, sub):
    assert(context.calculator.subtract() == int(sub))

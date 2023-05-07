from behave import *


@given(u'I have an invalid user')
def step_impl(context):
    print(u'STEP: Given I have an invalid user')


@given(u'an invalid password')
@when(u'I send them to the login form')
def step_impl(context):
    print(u'STEP: When I send them to the login form')


@then(u'wrong text message will be displayed on the screen')
def step_impl(context):
    print(u'STEP: Then wrong text message will be displayed on the screen')


@given(u'I have an valid user')
def step_impl(context):
    print(u'STEP: Given I have an valid user')

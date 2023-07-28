from behave import *
from features.pageobject.RegisterPage import RegisterPage
from features.pageobject.Homepage import Homepage
@when(u'user clicks the myaccount element')
def step_impl(context):
    context.Homepage=Homepage(context.driver)
    context.RegisterPage=context.Homepage.click_myAccount()

@when(u'user clicks the register button')
def step_impl(context):
    context.Homepage.click_register()
@then(u'verify user navigate to the register page')
def step_impl(context):
    assert context.RegisterPage.verify_registerPage("Register Account")


@then(u'enter the below records in the required field')
def step_impl(context):
    for row in context.table:
        context.RegisterPage.enter_fname(row["firstname"])
        context.RegisterPage.last_name(row["lastname"])
        context.RegisterPage.enter_telephone(row["telephone"])
        context.RegisterPage.email(row["email"])
        context.RegisterPage.enter_password(row["password"])
        context.RegisterPage.re_enter_pwd(row["reenterpwd"])
    # context.RegisterPage.enter_fname('vijay')
    # context.RegisterPage.last_name('mp')
    # context.RegisterPage.enter_telephone('978965432')
    # context.RegisterPage.email('pskumar123@gmail.com')
    # context.RegisterPage.enter_password('password55')
    # context.RegisterPage.re_enter_pwd('password55')


@then(u'tick the privacy policy and click continue button')
def step_impl(context):
    context.RegisterPage.click_privacy()
    context.RegisterPage.click_continue()


@then(u'verify that user launched in account page')
def step_impl(context):
    context.RegisterPage.verify_account_created_page()
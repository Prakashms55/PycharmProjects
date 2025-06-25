from behave import *
from features.pageobject.Homepage import Homepage


@given(u'verify user navigate to the home page')
def step_impl(context):
    context.homepage=Homepage(context.driver)
    assert context.homepage.verify_homePage("Your Store")

@when(u'user enter the product in the search box')
def step_impl(context):
    context.homepage.send_keys_searchBar("hp")

@when(u'user the click the search button')
def step_impl(context):
    context.searchPage=context.homepage.click_search()

@then(u'verify user navigate to the product page')
def step_impl(context):
  assert context.searchPage.verify_page()


@when(u'user enter the invalid product in the search box')
def step_impl(context):
    context.homepage.send_keys_searchBar("honda")

@then(u'verify user get the proper message')
def step_impl(context):
    assert context.searchPage.verify_proper_message()
@when(u'user enter nothing in the search box')
def step_impl(context):
    context.homepage.send_keys_searchBar("")

@then(u'proper message should be displayed')
def step_impl(context):
    assert context.searchPage.verify_proper_message()

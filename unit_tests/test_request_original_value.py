from pytest_bdd import given, when, then, scenarios

from boofuzz import Request
from boofuzz import primitives

scenarios('request_original_value.feature')


@given('A Request with one block')
def request_one_block(context):
    r = Request("unit-test-request")
    r.push(primitives.Byte(value=0, name="byte block"))
    context.request = r


@given('A Request with multiple blocks')
def request_multiple_blocks(context):
    r = Request("unit-test-request")
    r.push(primitives.Byte(value=1, name="string block"))
    r.push(primitives.String(value="The perfection of art is to conceal art.", name="unit-test-byte"))
    context.request = r


@given('Request is mutated once')
def mutate_once(context):
    context.request.mutate()


@given('Request is mutated twice')
def mutate_twice(context):
    context.request.mutate()
    context.request.mutate()


@given('Request is mutated thrice')
def mutate_twice(context):
    context.request.mutate()
    context.request.mutate()
    context.request.mutate()


@when('Calling original_value')
def call_original_value(context):
    context.result = context.request.original_value


@then('Result equals .render()')
def result_equals_render(context):
    assert context.result == context.request.render()


@then('Result equals .render() after .reset()')
def result_equals_render_after_reset(context):
    context.request.reset()
    assert context.result == context.request.render()

# class TestRequestOriginalValue(unittest.TestCase):
#     def test_same_as_initial_render_1_block(self):
#         """
#         Given A Request with one block
#         When Calling original_value
#         Then Result equals .render()
#         """
#         pass
#
#     def test_same_as_initial_render_many_blocks(self):
#         """
#         Given A Request with multiple blocks
#         When Calling original_value
#         Then Result equals .render()
#         """
#         pass
#
#     def test_same_as_initial_render_after_mutate(self):
#         """
#         Given A Request with multiple_blocks mutated once
#         When Calling original_value
#         Then Result equals .render()
#         """
#         pass
#
#     def test_same_as_initial_render_after_2_mutations(self):
#         """
#         Given A Request with multiple_blocks mutated twice
#         When Calling original_value
#         Then Result equals .render()
#         """
#         pass

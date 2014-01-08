import colander
from deform import Form
from deform.widget import SequenceWidget
from kotti.interfaces import IContent
from kotti.views.util import template_api
from pyramid.view import view_config


@view_config(name='view',
             context=IContent,
             permission='view',
             renderer='kotti_test:templates/test.pt')
def view_test(context, request):

    class FormSchema(colander.MappingSchema):

        class Tests(colander.SequenceSchema):
           test = colander.SchemaNode(colander.String())

        tests = Tests(
            validator = colander.Length(2, 4),
            title = 'At Least 2 At Most 4 Tests',
            widget=SequenceWidget(
                min_len=2,
                max_len=4
            )
        )

    return {
        'form': Form(FormSchema()).render(),
        'api': template_api(context, request),
    }

import _plotly_utils.basevalidators


class RangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self,
        plotly_name='range',
        parent_name='layout.polar.radialaxis',
        **kwargs
    ):
        super(RangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'axrange'),
            implied_edits=kwargs.pop('implied_edits', {'autorange': False}),
            items=kwargs.pop(
                'items', [
                    {
                        'valType': 'any',
                        'editType': 'axrange',
                        'impliedEdits': {
                            '^autorange': False
                        }
                    }, {
                        'valType': 'any',
                        'editType': 'axrange',
                        'impliedEdits': {
                            '^autorange': False
                        }
                    }
                ]
            ),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )

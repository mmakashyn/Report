import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from wagtail.core import hooks


@hooks.register('register_rich_text_features')
def register_bluehighlight_feature(features):
    feature_name = 'cm_blue'
    type_ = 'BLUE_HIGHLIGHT'
    tag = f'span{feature_name}'

    control = {
        'type': type_,
        'label': 'Blue',
        'description': 'Blue text color',
        'style': {'color': '#00b8ed'},
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'class': 'txt-color cm-blue'
                    }
                }
            }
        },
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

@hooks.register('register_rich_text_features')
def register_lightbluehighlight_feature(features):
    feature_name = 'cm_light_blue'
    type_ = 'LIGHT_BLUE_HIGHLIGHT'
    tag = f'span{feature_name}'

    control = {
        'type': type_,
        'label': 'Light Blue',
        'description': 'Light Blue text color',
        'style': {'color': 'rgb(132, 171, 195)'},
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'class': 'txt-color cm-light-blue'
                    }
                }
            }
        },
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

@hooks.register('register_rich_text_features')
def register_pinkhighlight_feature(features):
    feature_name = 'cm_red'
    type_ = 'PINK_HIGHLIGHT'
    tag = f'span{feature_name}'

    control = {
        'type': type_,
        'label': 'Red',
        'description': 'Red text color',
        'style': {'color': '#ff0000'},
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'class': 'txt-color cm-red'
                    }
                }
            }
        },
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)


@hooks.register('register_rich_text_features')
def register_orangehighlight_feature(features):
    feature_name = 'cm_orange'
    type_ = 'ORANGE_HIGHLIGHT'
    tag = 'span'
    tag = f'span{feature_name}'

    control = {
        'type': type_,
        'label': 'Orange',
        'description': 'Orange text color',
        'style': {'color': '#ff9619'},
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'class': 'txt-color cm-orange'
                    }
                }
            }
        },
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)


@hooks.register('register_rich_text_features')
def register_greenhighlight_feature(features):
    feature_name = 'cm_green'
    type_ = 'GREEN_HIGHLIGHT'
    tag = f'span{feature_name}'

    control = {
        'type': type_,
        'label': 'Green',
        'description': 'Green text color',
        'style': {'color': '#00d6aa'},
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'id': type_,
                        'class': 'txt-color cm-green'
                    }
                }
            }
        },
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)
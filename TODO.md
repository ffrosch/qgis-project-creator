# TODO

- [ ] extend the `after_create` method, so that non-spatial tables are also added to and removed from the `gpkg_contents` table, see [here](https://github.com/geoalchemy/geoalchemy2/blob/master/geoalchemy2/admin/dialects/geopackage.py#L228)

## Necessary order of operations

1. init qgis/project
1. create gpkg
1. create layers
1. create relations
1. create widgets
1. create attribute forms
1. save project

## Extending SQLAlchemy `Column` - Ideas

- Inherit from Column and define custom init-function that pops my custom keyword argument before super().**init**(...) is called
- Monkey-patch `sqlalchemy.sql.schema.Column._extra_kwargs` (line 2251)
- ✅ use `info` keyword from `MappedColumn`
- using a [mapper](https://gist.github.com/hjwp/09fd282062e934eeb2a46a40945e48c8), also described in the [Declarative Dataclass Mapping](https://docs.sqlalchemy.org/en/20/orm/dataclasses.html#orm-declarative-native-dataclasses) section of SQLAlchemy

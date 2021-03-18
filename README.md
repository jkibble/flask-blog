flask blog app

## add new language
`pybabel init -i messages.pot -d blog/translations -l <language_code>`

## extract translations
`pybabel extract -F babel.cfg  -o messages.pot .`

## update / add translations to existing message.po files
`pybabel update -i messages.pot -d blog/translations`

## compile translations to message.mo file(s)
`pybabel compile -d  blog/translations`


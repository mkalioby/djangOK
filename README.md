# djangOK
Runs Django check  to make sure code is Ok.

Can be installed as a pre-commit

```yaml
repos:
        - repo: https://github.com/mkalioby/djangOK
          rev: a175263
          hooks:
             - id: djangOK
               args: []
```

there is an optional argument which is the folder path of `manage.py`

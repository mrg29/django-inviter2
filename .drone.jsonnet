local Pipeline(name, image, django) = {
  kind: "pipeline",
  name: name,
  steps: [
    {
      name: "test",
      image: image,
      environment: {
        DJANGO: django
      },
      commands: [
        "pip install $DJANGO coveralls",
        "python setup.py develop",
        "coverage run example/manage.py test -v2"
      ]
    }
  ]
};

[
  Pipeline("py2.7+Dj1.7", "python:2.7", "Django>=1.7,<1.8"),
  Pipeline("py2.7+Dj1.8", "python:2.7", "Django>=1.8,<1.9"),
  Pipeline("py2.7+Dj1.9", "python:2.7", "Django>=1.9,<1.10"),
  Pipeline("py3.3+Dj1.7", "python:3.3", "Django>=1.7,<1.8"),
  Pipeline("py3.3+Dj1.8", "python:3.3", "Django>=1.8,<1.9"),
  Pipeline("py3.4+Dj1.7", "python:3.4", "Django>=1.7,<1.8"),
  Pipeline("py3.4+Dj1.8", "python:3.4", "Django>=1.8,<1.9"),
  Pipeline("py3.4+Dj1.9", "python:3.4", "Django>=1.9,<1.10"),
  Pipeline("py3.5+Dj1.8", "python:3.5", "Django>=1.8,<1.9"),
  Pipeline("py3.5+Dj1.9", "python:3.5", "Django>=1.9,<1.10"),
]

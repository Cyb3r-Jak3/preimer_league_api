.PHONY: clean clean-build clean-pyc test docs

clean: clean-build clean-pyc

full-test: lint test

ifeq ($(OS),Windows_NT)
    RM = del //Q //F
    RRM = rmdir //Q //S
else
    RM = rm -f
    RRM = rm -f -r
endif

clean-build:
	$(RM) -r build/
	$(RM) -r dist/
	$(RM) -r *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec $(RM) {} +
	find . -name '*.pyo' -exec $(RM) {} +
	find . -name '*~' -exec $(RM) {} +

build:
	python setup.py sdist bdist_wheel

check-dist:
	pip install wheel twine --quiet
	python setup.py egg_info
	python setup.py sdist bdist_wheel
	twine check --strict dist/*

lint:
	black --check premier_league_api
	pylint --disable=invalid-name premier_league_api
	flake8 --max-line-length 100 --ignore=F403,F401 --statistics --show-source --count premier_league_api
	bandit -r premier_league_api

test:
	py.test --cov premier_league_api tests/ -vv
	black premier_league_api

gen_comps:
	python -c "import premier_league_api; premier_league_api.create_competitions_file()"
	black premier_league_api/competitions.py

docs:
	sphinx-apidoc -f -o docs/ premier_league_api
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
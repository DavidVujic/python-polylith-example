.PHONY: export-deps build-project gcp-package

PROJECT_NAME = my_gcp_function_project-0.1.0

export-deps:
	poetry export -f requirements.txt --output requirements.txt

build-project: export-deps
	poetry build-project

gcp-package: build-project
	mv dist/$(PROJECT_NAME)-py3-none-any.whl dist/function.zip

run-dev:
	find src -type d -name '__pycache__' -exec rm -r {} + && python -B -m src.main

format:
	uv run ruff format .
	uv run ruff check --fix .

check:
	@echo "1/2 Running Ruff (Linting & Formatting check)..."
	uv run ruff check .
	uv run ruff format --check .
	@echo "2/2 Running Basedpyright (Type checking)..."
	uv run basedpyright

clean:
	rm -rf .ruff_cache .basedpyright_cache .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +

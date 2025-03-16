lint:
	git add .
	pre-commit run --all-files
	@git diff --quiet || (git add . && echo "Staged modified files")

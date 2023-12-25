from huggingface_hub import HfApi, Repository

api = HfApi()
repo_url = api.create_repo(token="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", name="project-scheduling-nlp-dataset", type="dataset")
repo = Repository("project-scheduling-nlp-dataset", clone_from=repo_url)
repo.git_add()
repo.git_commit("Add project-scheduling-nlp dataset")
repo.git_push()
import json
from pathlib import Path
from experiment import Experiment

lab_folder = Path(__file__).resolve().parent
json_path = lab_folder / "data" / "experiments.json"
report_path = lab_folder / "reports" / "experiment_summary.txt"

#Shan_72387_PFAI_Week04
def add_experiment(experiments, experiment_id, model_name, dataset_name, accuracy):
  exp = Experiment(experiment_id, model_name, dataset_name, accuracy)
  experiments.append(exp)
  return exp

#Shan_72387_PFAI_Week04
def display_experiments(experiments):
  if not experiments:
    print("No experiments are available")
    return

  for exp in experiments:
    print(
        f"{exp.experiment_id} | {exp.model_name} | {exp.dataset_name} |"
        f" Accuracy: {exp.accuracy}"
    )

#Shan_72387_PFAI_Week04
def search_experiment(experiments, experiment_id):
  for exp in experiments:
    if exp.experiment_id == experiment_id:
      return exp
  return None


def find_best_experiment(experiments):
  if not experiments:
    return None
  return max(experiments, key=lambda experiment: experiment.accuracy)

#Shan_72387_PFAI_Week04
def save_experiments(experiments, file_path):
  """ Save experiments to a JSON file."""
  path = Path(file_path)
  path.parent.mkdir(parents=True, exist_ok=True)
  records = [exp.to_dictionary() for exp in experiments]
  with open(path, "w", encoding="utf-8") as file:
    json.dump(records, file, indent=4)

#Shan_72387_PFAI_Week04
def load_experiments(file_path):
  """Load experiments from JSON."""
  json_path = Path(file_path)
  if not json_path.exists():
    return []
  try:
    with open(json_path, "r", encoding="utf-8") as file:
      records = json.load(file)
      return [
          Experiment(
              r["experiment_id"],
              r["model_name"],
              r["dataset_name"],
              r["accuracy"],
          )
          for r in records
      ]
  except json.JSONDecodeError:
    print("Invalid JSON data detected.")
    return []

#Shan_72387_PFAI_Week04
def write_summary(experiments, file_path):
  path = Path(file_path)
  path.parent.mkdir(parents=True, exist_ok=True)
#Shan_72387_PFAI_Week04
  lines = ["=== Experiment Summary Report ==="]
  for exp in experiments:
    lines.append(f"{exp.experiment_id} | {exp.model_name} | Accuracy: {exp.accuracy}")

  best = find_best_experiment(experiments)
  if best:
    lines.append("\n=== Best Experiment ===")
    lines.append(
        f"{best.experiment_id} | {best.model_name} | Accuracy: {best.accuracy}"
    )

  with open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))


def run_assertions():
 #Shan_72387_PFAI_Week04
  exp = Experiment("TEST-1", "Model", "Data", "0.85")
  assert isinstance(exp.accuracy, float) and exp.accuracy == 0.85

 #Shan_72387_PFAI_Week04
  data_dict = exp.to_dictionary()
  assert data_dict == {
      "experiment_id": "TEST-1",
      "model_name": "Model",
      "dataset_name": "Data",
      "accuracy": 0.85,
  }

  test_list = [
      exp,
      Experiment("TEST-2", "Model2", "Data", 0.95),
  ]

 #Shan_72387_PFAI_Week04
  assert search_experiment(test_list, "TEST-1") == exp

#Shan_72387_PFAI_Week04
  assert search_experiment(test_list, "UNKNOWN") is None

 #Shan_72387_PFAI_Week04
  best = find_best_experiment(test_list)
  assert best.experiment_id == "TEST-2" and best.accuracy == 0.95

 #Shan_72387_PFAI_Week04
  try:
    Experiment("TEST-FAIL", "Model", "Data", 1.5)
    assert False, "Should have raised ValueError for accuracy > 1"
  except ValueError:
    pass

  try:
    Experiment("TEST-FAIL", "Model", "Data", -0.1)
    assert False, "Should have raised ValueError for accuracy < 0"
  except ValueError:
    pass


def main():
#Shan_72387_PFAI_Week04
  run_assertions()

 
  experiments = load_experiments(json_path)

#Shan_72387_PFAI_Week04
  print(f"Loaded {len(experiments)} records at startup.")

 #Shan_72387_PFAI_Week04
  if not experiments:
    add_experiment(
        experiments, "EXP-001", "Logistic Regression", "Student Performance", 0.84
    )
    add_experiment(
        experiments, "EXP-002", "Decision Tree", "Student Performance", 0.88
    )
    add_experiment(
        experiments, "EXP-003", "kNN", "Student Performance", 0.91
    )

 #Shan_72387_PFAI_Week04
  print("\n--- All Experiments ---")
  display_experiments(experiments)


  print("\n--- Search Result ---")
  found = search_experiment(experiments, "EXP-002")
  if found is not None:
    print(found.to_dictionary())
  else:
    print("Experiment was not found.")

 
  best = find_best_experiment(experiments)
  print("\n--- Best Experiment ---")
  if best:
    print(best.to_dictionary())

#Shan_72387_PFAI_Week04
  save_experiments(experiments, json_path)


  write_summary(experiments, report_path)


  reloaded_experiments = load_experiments(json_path)


  print(f"\nSuccessfully reloaded {len(reloaded_experiments)} records.")

#Shan_72387_PFAI_Week04
  assert len(reloaded_experiments) == len(experiments)


if __name__ == "__main__":
  main()
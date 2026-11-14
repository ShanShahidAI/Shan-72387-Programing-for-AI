class Experiment:

  def __init__(self, experiment_id, model_name, dataset_name, accuracy):
    try:#Shan_72387_PFAI_Week04
      acc = float(accuracy)
    except (ValueError, TypeError):
      raise ValueError(f"Accuracy must be a valid number, got: {accuracy}")

    if not (0 <= acc <= 1):
      raise ValueError(
          f"Accuracy must be between 0 and 1, got: {accuracy}"
      )
#Shan_72387_PFAI_Week04
    self.experiment_id = experiment_id
    self.model_name = model_name
    self.dataset_name = dataset_name
    self.accuracy = acc
#Shan_72387_PFAI_Week04
  def to_dictionary(self):
    return {
        "experiment_id": self.experiment_id,
        "model_name": self.model_name,
        "dataset_name": self.dataset_name,
        "accuracy": self.accuracy,
    }
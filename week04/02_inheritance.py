"""Inheritance and method overriding demonstration for AI models."""
class AIModel:
    """Base class for all AI models."""

    def __init__(self, model_name):
        self.model_name = model_name
        self.is_trained = False
#Shan_72387_PFAI_Week04
    def train(self):
        """Simulate model training state."""
        self.is_trained = True

    def describe(self):
        """Return generic model description."""
        return f"Model: {self.model_name}"
#Shan_72387_PFAI_Week04
class ClassificationModel(AIModel):
    """Subclass representing categorical prediction models."""

    def __init__(self, model_name, classes):
        super().__init__(model_name)
        self.classes = classes
#Shan_72387_PFAI_Week04
    def describe(self):
        """Override describe to include target classes."""
        return f"{super().describe()} | Classes: {self.classes}"

class RegressionModel(AIModel):
    """Subclass representing continuous prediction models."""
#Shan_72387_PFAI_Week04
    def __init__(self, model_name, target_name):
        super().__init__(model_name)
        self.target_name = target_name

    def describe(self):
        """Override describe to include continuous target name."""
        return f"{super().describe()} | Target: {self.target_name}"
#Shan_72387_PFAI_Week04
def main():
    """Create models, run training, and display profiles."""
    clf = ClassificationModel("Random Forest", ["Cat", "Dog"])
    reg = RegressionModel("Linear Regression", "House Price")

    clf.train()
    reg.train()

    print(f"{clf.describe()} | Trained: {clf.is_trained}")
    print(f"{reg.describe()} | Trained: {reg.is_trained}")

#Shan_72387_PFAI_Week04
if __name__ == "__main__":
    main()

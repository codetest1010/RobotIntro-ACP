class robot:
  """Represents a robot with a name, model, and purpose."""
  
  def __init__(self, name, model, purpose):
    """Initializes a new Robot instance."""
    self.name = name
    self.model = model
    self.purpose = purpose
    
  def introduce(self):
    """Introduces the robot."""
    print(f"Hello, I am {self.name}, a {self.model} robot.")
    print(f"My purpose is to {self.purpose}.")

# Create a robot instance
my_robot = robot("R2-D2", "Astromech Droid", "assist with repairs and navigation")

# Introduce the robot
my_robot.introduce()
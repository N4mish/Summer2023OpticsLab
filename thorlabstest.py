from pylablib.devices import Thorlabs

stage = Thorlabs.KinesisMotor("55000784", is_rack_system=True, scale="K10CR1")
stage.move_to(0)
stage.wait_move()

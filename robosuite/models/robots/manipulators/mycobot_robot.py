import numpy as np

from robosuite.models.robots.manipulators.manipulator_model import ManipulatorModel
from robosuite.utils.mjcf_utils import xml_path_completion


class MyCobot(ManipulatorModel):
    """
    Mycobot is a sensitive single-arm robot

    Args:
        idn (int or str): Number or some other unique identification string for this robot instance
    """

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("robots/mycobot/robot.xml"), idn=idn)

        # Set joint damping
        self.set_joint_attribute(attrib="damping", values=np.array((0.1, 0.1, 0.1, 0.1, 0.01, 0.01)))
        
        #self.init_qpos = np.array((0.1, 0.1, 0.1, 0.1, 0.01, 0.01))

    @property
    def default_mount(self):
        return None
        #return "RethinkMount"
        #return "Table"
        #return "RethinkMinimalMount"
    @property
    def bottom_offset(self):
        """
        Returns vector from model root body to model bottom.
        By default, this is equivalent to this robot's mount's (bottom_offset - top_offset) + this robot's base offset

        Returns:
            np.array: (dx, dy, dz) offset vector
        """
        return (
            (self.mount.bottom_offset - self.mount.top_offset) + self._base_offset
            if self.mount is not None
            else self._base_offset 
            
        )

    # TODO
    @property
    def default_gripper(self):
        return "MyCobotGripper"
        #return "PandaGripper" 
        #return 

    # TODO
    @property
    def default_controller_config(self):
        return "default_panda"

    @property
    def init_qpos(self):
        #return np.array([0, np.pi / 16.0, 0.00, -np.pi / 2.0 - np.pi / 3.0, 0.00, np.pi - 0.2, ])
        return np.zeros(6)
        #return np.array([np.pi / 16.0, 0.00, -np.pi / 2.0 - np.pi / 3.0, 0.00, np.pi - 0.2, np.pi / 4])

    @property
    def base_xpos_offset(self):
        return {
            "bins": (-0.5, -0.1, 0),
            "empty": (-0.6, 0, 0),
            #"table": lambda table_length: (-0.16 - table_length / 2, 0, 0),
            "table": lambda table_length: (-table_length/2 + 0.05, 0, 0.8),
        }

    @property
    def top_offset(self):
        return np.array((0, 0, 5.0))

    @property
    def _horizontal_radius(self):
        return 0.5

    @property
    def arm_type(self):
        return "single"
    
    @property
    def _eef_name(self):
        return "link6"
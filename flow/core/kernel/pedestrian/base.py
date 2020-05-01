"""Script containing the base pedestrian kernel class."""

class KernelPedestrian(object):
    """Flow pedestrian kernel.

    """

    def __init__(self,
            master_kernel):
        """Instantiate the Flow pedestrian kernel.

        Parameters
        ----------
        master_kernel: flow.core.kernel.Kernel
            the higher level kernel (used to call methods from other
            sub-kernels)
        """
        self.master_kernel = master_kernel
        self.kernel_api = None

    def pass_api(self, kernel_api):
        """Acquire the kernel api that was generated by the simulation kernel.

        Parameters
        ----------
        kernel_api : any
            an API that may be used to interact with the simulator.
        """
        self.kernel_api = kernel_api

    def update(self, reset):
        """Update the vehicle kernel with data from the current time step.
        
        This method is used to optimize the computational efficiency of
        acquiring pedestrians state information from the kernel.

        Parameters
        ----------
        reset : bool
            specifies whether the simulator was reset in the last simulation
            step
        """
        raise NotImplementedError

    def add(self, ped_id, edge, pos, lane, speed):
        """Add a pedestrian to the network.

        Parameters
        ----------
        ped_id : str
            unique identifier of the pedestrians to be added
        edge : str
            edge the pedestrian will get added to
        pos : float
            position along the edge the pedestrian will get added
        lane : int
            lane on which the pedestrian will get added
        speed : float
            starting speed of the pedestrians

        """
        raise NotImplementedError

    def get_next_edge(self, ped_id):
        """getNextEdge() -> string

        If the person is walking, returns the next edge on the persons route
        (including crossing and walkingareas). If there is no further edge or the
        person is in another stage, returns the empty string.
        """
        raise NotImplementedError


    def remove(self, ped_id):
        """Remove a pedestrian.

        This method removes all traces of the pedestrian from the pedestrians
        kernel.

        In addition, if the pedestrian is still in the network, this method calls
        the necessary simulator-specific commands to remove it.

        Parameters
        ----------
        ped_id : str
            unique identifier of the pedestrian to be removed
        """
        raise NotImplementedError

    ############################################################################
    #                          State acquisition methods                       #
    ############################################################################
    
    def get_speed(self, ped_if, error=-1001):
        """ Returns the speed of the pedestrian.
        
        Parameters
        ----------
        ped_id : str or list of str
            pedestrian id, or list of pedestrian ids
        error : any, optional
            value that is returned if the pedestrian is not found

        Returns
        -------
        float
        """
        raise NotImplementedError

    def get_position(self, ped_id, error=-1001):
        """ Returns the position of the pedestrian relative to its current edge.
        
        Parameters
        ----------
        ped_id : str or list of str
            pedestrian id, or list of pedestrian ids
        error : any, optional
            value that is returned if the pedestrian is not found

        Returns
        -------
        float
        """
        raise NotImplementedError

    def get_lane_position(self, ped_id, error=-1001):
        """Returns the position of the person along the lane / edge measured in m.
        
        Make sure to check what the 'start' of a lane / edge is.
        """
        raise NotImplementedError

    def get_edge(self, ped_id, error=""):
        """ Returns the edge the specified pedestrian is currently on.

        Parameters
        ----------
        ped_id : str or list of str
            pedestrian id, or list of pedestrian ids
        error : any, optional
            value that is returned if the pedestrian is not found

        Returns
        -------
        str
        """
        raise NotImplementedError

    ############################################################################
    #                             State setting methods                        #
    ############################################################################

    def set_speed(self, ped_id, speed, error=-""):
        """Sets the maximum speed in m/s for the named person for subsequent step.
        TODO(KL) Subsequent step = immediate next step only?

        Parameters
        ----------
        ped_id : str or list of str
            pedestrian id, or list of pedestrian ids
        speed : double
            maximum speed in m/s for the named person for subsequent step.

        Returns
        -------
        None
        """
        raise NotImplementedError
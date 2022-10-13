import numpy as np


def geo_stationary_trajectory(h, r):
    """
    Calculate the trajectory of a satellite in a geostationary orbit.
    Parameters
    ----------
    h : float
    Height of the satellite above the surface of the Earth, in kilometers.
    r : float
    Radius of the Earth, in kilometers.
    Returns
    -------
    array_like
    The trajectory of the satellite, as a sequence of (x, y, z) tuples
    in kilometers.
    """
    # Set the starting point of the trajectory
    x = h + r
    y = 0.0
    z = 0.0
    # Set the starting velocity of the trajectory
    vx = 0.0
    vy = np.sqrt(3.986004418e14 / (x + r))  # Orbital velocity
    vz = 0.0
    # Set the time step for the trajectory
    dt = 60.0  # One minute
    # Initialize the trajectory array
    trajectory = [(x, y, z)]
    # Calculate the trajectory
    while True:
        # Calculate the next position of the satellite
        x, y, z, vx, vy, vz = predict_position(x, y, z, vx, vy, vz, dt,r)
        # Add the position to the trajectory array
        trajectory.append((x, y, z))
        # If we've gone around the Earth once, we're done
        if x < h + r:
            break
    # Return trajectory
    return trajectory



def predict_position(x, y, z, vx, vy, vz, dt,r):
    """
    Calculate the position of an object after a time dt, given its
    position, velocity, and acceleration.
    Parameters
    ----------
    x : float
    The object's initial x-position.
    y : float
    The object's initial y-position.
    z : float
    The object's initial z-position.
    vx : float
    The object's initial x-velocity.
    vy : float
    The object's initial y-velocity.
    vz : float
    The object's initial z-velocity.
    dt : float
    The time step to take.
    Returns
    -------
    tuple
    A tuple (x, y, z, vx, vy, vz) giving the object's position and velocity
    after time dt.
    """
    # Calculate the acceleration due to gravity
    ax = -3.986004418e14 * x / ((x + r)**3)
    ay = -3.986004418e14 * y / ((y + r)**3)
    az = -3.986004418e14 * z / ((z + r)**3)
    # Calculate the next position of the object
    x = x + vx * dt + 0.5 * ax * dt**2
    y = y + vy * dt + 0.5 * ay * dt**2
    z = z + vz * dt + 0.5 * az * dt**2
    # Calculate the next velocity of the object
    vx = vx + ax * dt
    vy = vy + ay * dt
    vz = vz + az * dt
    # Return position and velocity of the object

    #edited
    return x,y,z,vx,vy,vz
   


def get_satellite_position(t, h, v):
    """
    Calculate position od satellite in the orbit given it height and velocity after given
    time.
    Parameters
    ----------
    t : float
    is the time in seconds
    h : float
    is the height of the satellite in kilometers
    v : float
    is the velocity of the satellite in kilometers per second
    Returns
    -------
    position : numpy.array
    An array (x, y, z) giving the object's position.
    velocity : numpy.array
    An array (vx, vy, vz) giving the object's velocity.
    t0 : float
    time in seconds since epoch
    """
    G = 6.67300 * 10**-11  # N*(m/kg)^2
    M = 5.972 * 10**24  # kg
    r = h + 6371  # km
    a = ((G * M) / (r * v)) * (1 - (h/r)**2)**-0.5  # km
    e = np.sqrt(1 - (h/a)**2)
    P = a * (1 - e**2)  # km
    b = (P/e)**0.5
    i = np.arccos(h/r)  # rad
    # RAAN
    Omega = 0  # rad
    # Perigee Argument
    w = 0  # rad
    # True Anomaly
    theta = 2 * np.arctan(((1 + e)/(1 - e))**0.5
                          * np.tan(v/2))  # rad
    # Eccentric Anomaly
    E = 2 * np.arctan(((1 - e)/(1 + e))**0.5 * np.tan(theta/2))  # rad
    # Mean Anomaly
    M = E - e * np.sin(E)  # rad
    # Time since perigee
    T = (M * np.sqrt(a**3 / M)) / (2 * np.pi)  # seconds
    # Time since Epoch
    t0 = t - T  # seconds
    # Orbital elements
    n = 2 * np.pi * np.sqrt((G * M)/(a**3))
    #Position in Orbit
    r = a * (1 - e**2) / (1 + e * np.cos(theta))  # km
    x = r * np.cos(theta + w)
    y = r * np.sin(theta + w)
    z = 0
    #Velocity in Orbit
    v = (2 * np.pi * a) / (P * np.sqrt(1 - e**2))
    vx = -v * np.sin(theta + w)
    vy = v * np.cos(theta + w)
    vz = 0
    # Return numpy array of position and velocity and time since Epoch


    # edited
    return [x, y, z], [vx, vy, vz], t0


if __name__ == "__main__":
    trajectory = geo_stationary_trajectory(35786, 6378)
    position, velocity, time = get_satellite_position(
        756683108271174, 2000, 7.79)

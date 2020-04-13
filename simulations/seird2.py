import numpy as np 



def seird_simulate(x, n_days=120, dt=0.1):

    initially_exposed = x[0]
    R0 = x[1]
    IIC = x[2]
    IDC = 0.5

    ICR = x[3]

    effective_incubation_period = 5
    effective_infectious_duration = 2 # For what duration will the infectant be infectous
    effective_time_in_ICU = 5

    alpha = 1 / effective_incubation_period
    beta = R0 / effective_infectious_duration
    gamma = 1 / effective_infectious_duration
    kappa = 1 / effective_time_in_ICU

    # initialization
    days = [0]
    exposed = [initially_exposed]
    infectious = [0] 
    susceptibles = [1 - exposed[0]]
    recovered = [0]
    confirmed = [0]
    icutreated = [0]
    deceased = [0]
    checksum = [1]
    dailyconfirmed = [0]
    dailydeceased = [0]
    confirmed_out = []
    deceased_out = []
    days_out = []
    t = 0

    # simulations
    while t < n_days:

        new_exposed = beta * infectious[-1] * susceptibles[-1] * dt
        new_infectious = alpha * exposed[-1] * dt
        new_recovered_normal = (1 - IIC) * gamma * infectious[-1] * dt 
        new_in_icutreatment = IIC * gamma * infectious[-1] * dt
        new_recovered_from_icu = (1 - IDC) * kappa * icutreated[-1] * dt
        new_deceased =  IDC * kappa * icutreated[-1] * dt

        susceptibles.append(susceptibles[-1] - new_exposed)
        infectious.append(infectious[-1] + new_infectious - new_recovered_normal - new_in_icutreatment)   
        recovered.append(recovered[-1] + new_recovered_normal + new_recovered_from_icu)
        exposed.append(exposed[-1] + new_exposed - new_infectious)
        icutreated.append(icutreated[-1] + new_in_icutreatment - new_recovered_from_icu - new_deceased)
        deceased.append(deceased[-1] + new_deceased)

        confirmed.append(confirmed[-1] + ICR * new_infectious)
        dailyconfirmed.append(ICR * new_infectious / dt) 
        dailydeceased.append(new_deceased / dt)


        checksum.append(infectious[-1] + recovered[-1] + susceptibles[-1] + exposed[-1] + deceased[-1] + icutreated[-1])
        t = t + dt

        if int(t-dt/2) != int(t+dt/2):
            confirmed_out.append(confirmed[-1])
            deceased_out.append(deceased[-1])
            days_out.append(t)
            


        days.append(t)

    output =  {
        'time': days_out,
        'confirmed': confirmed_out,
        'deceased': deceased_out,
        'plot_data': {
            'time': days,
            'susceptibles': susceptibles,
            'exposed': exposed,
            'infectious': infectious,
            'icutreatment': icutreated,
            'recovered': recovered,
            'deceased': deceased,
            'checksum': checksum,
            'daily_confirmed': dailyconfirmed,
            'daily_deceased': dailydeceased
        }
    }

    return output

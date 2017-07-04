# OOP_hospital
This demonstrates the working of an ordinary clinic using object oriented programming concepts

## Usage 
```
from hospital import Hospital 

# add doctor
Hospital.add_doctor('Paul','Nyondo','M')

# add doctor
Hospital.add_patient('Sirius','Black','M')

#treat patient 
Hospital.treat(0,0) #doctor_id and patient_id

#discharge patient
Hospital.discharge()

```

Other attributes of the clinic can be gotten such as number of patients, doctors 

```
    # get number of doctors
    Hospital.num_of_doctors

    #get number of patients
    Hospital.num_of_patients

```



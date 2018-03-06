-- query the voltage for measurement 1
select c.voltage  
from measurements a  
join measurement_voltage b 
on a.id = b.measurement_id  

join voltages c 
on b.voltage_id = c.id  
where a.id = 1 ;

-- query the frequency
select e.frequency 
from measurements a  
join measurement_frequency d 
on a.id = d.measurement_id  

join frequencies e 
on d.frequency_id = e.id  
where a.id = 1;

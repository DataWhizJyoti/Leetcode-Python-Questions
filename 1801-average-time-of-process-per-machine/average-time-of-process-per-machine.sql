# Write your MySQL query statement below

with cte as(
select t1.machine_id, t1.process_id, t1.timestamp as start_time, t2.timestamp as end_time
from Activity t1,Activity t2
where t1.machine_id=t2.machine_id and t1.process_id=t2.process_id and t1.activity_type="start" and t2.activity_type="end"
)
select machine_id, round((sum(end_time-start_time)/count(process_id)),3) as processing_time
from cte
group by machine_id
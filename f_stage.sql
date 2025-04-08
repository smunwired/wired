drop function f_stage;
delimiter //

CREATE DEFINER=`stef`@`%` FUNCTION `f_stage`(p_booking int,p_type int,p_direction int) RETURNS text CHARSET utf8mb3
    DETERMINISTIC
begin 
	declare done INT DEFAULT FALSE;
	declare v_str, v_concat text;
	declare v_counter int DEFAULT 0;
    declare v_dest text;
    declare v_direction text;
    
    declare cur1 cursor for
	select concat(stage_date,' ',f.nm,' : ',d1.cd,' -> ',d2.cd,' (',dptm,'->',artm,') ',seats,' seat(s)') 
       	from stage s 
	join bk_flight f on f.id = s.flight 
	left outer join bk_destination d1 on d1.id = dpdst 
	left outer join bk_destination d2 on d2.id = ardst 
	where booking=p_booking and direction=p_direction
	order by sequence;
	
    declare cur8 cursor for
	select concat(stage_date,' ',f.nm,' : ',d1.nm,' -> ',d2.nm,' (',dptm,') ',seats,' seat(s)') 
       	from stage s 
	join bk_flight f on f.id = s.flight 
	left outer join bk_destination d1 on d1.id = dpdst 
	left outer join bk_destination d2 on d2.id = ardst 
	where booking=p_booking and direction=p_direction
	order by sequence;
	
    declare cur2 cursor for
	select stage_date,d.nm,direction
       	from stage s join bk_destination d on d.id=s.destination 
	where booking=p_booking
	order by sequence;
	
    declare cur6 cursor for
	select concat(d.nm, ' on ' ,stage_date) 
       	from stage s join bk_destination d on d.id=s.destination 
	where booking=p_booking and direction=p_direction
	order by sequence;
	
    declare continue handler for not found set done = TRUE;
    
    if (p_type=1) then
	  open cur1;
	  stageLoop: loop
	    fetch cur1 into v_str;
	    if done then leave stageLoop; end if;
	    set v_counter = v_counter + 1;
	    if v_counter = 1 then 
		  set v_concat = v_str; 
	    else 
		  set v_concat = concat(v_concat,'<br/>',v_str); 
	    end if; 
	  end loop stageLoop;
	  close cur1;
    elseif (p_type=8) then
	  open cur8;
	  stageLoop: loop
	    fetch cur8 into v_str;
	    if done then leave stageLoop; end if;
	    set v_counter = v_counter + 1;
	    if v_counter = 1 then 
		  set v_concat = v_str; 
	    else 
		  set v_concat = concat(v_concat,'<br/>',v_str); 
	    end if; 
	  end loop stageLoop;
	  close cur8;
    elseif p_type=6 then 
	  open cur6;
	  stageLoop: loop
	    fetch cur6 into v_str;
	    if done then leave stageLoop; end if;
	    set v_counter = v_counter + 1;
	    if v_counter = 1 then 
		  set v_concat = v_str; 
	    else 
		  set v_concat = concat(v_concat,'<br/>',v_str); 
	    end if; 
	  end loop stageLoop;
	  close cur6;
    else 
	  open cur2;
	  stageLoop: loop
	    fetch cur2 into v_str,v_dest,v_direction;
	    if done then leave stageLoop; end if;
	    set v_counter = v_counter + 1;
	    if v_counter=1 and p_direction=0 then
          set v_concat = v_str; 
	    end if;
	    if v_counter=2 and p_direction=1 then
          set v_concat = v_str; 
	    end if;
	    if v_counter=2 and p_direction=2 then
          set v_concat = v_dest; 
	    end if;
	  end loop stageLoop;
	  close cur2;
    end if;
	return v_concat;
end//
delimiter ;


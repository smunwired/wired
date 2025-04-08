with u as (select nm,sz from filelist_wd_p 
except 
select nm,sz from filelist_live_p )
select url from filelist_wd_p f join u on u.nm=f.nm and u.sz=f.sz order by 1;

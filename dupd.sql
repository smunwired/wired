with u as (
select nm,sz from filelist_wdtb1_p 
where dr not like '/wdtb1-20240723/dev%'
--and dr not like '/media/public/live/dev%'
except 
select nm,sz from filelist_live_p )
select dr from filelist_wdtb1_p f join u on u.nm=f.nm and u.sz=f.sz group by dr order by 1;

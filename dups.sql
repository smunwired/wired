select nm,sz from filelist_wdtb1_p 
where dr not like '/wdtb1-20240723/dev%'
except 
select nm,sz from filelist_live_p 
order by 2 desc;

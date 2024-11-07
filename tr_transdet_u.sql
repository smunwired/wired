DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`stef`@`192.168.56.%`*/ /*!50003 TRIGGER `tr_transdet_u` BEFORE UPDATE ON `transdet` FOR EACH ROW begin

  set new.date_amended=now();

insert into transdet_audit (
        tran_id,tran_date,tran_creditor,tran_desc,tran_amount,
    cr_dr,tran_type_id,account_id,statement_date,cheque_no,
    receipt_ind,dd_ind,date_created,user_created,
    date_amended,user_amended,frequency,cred_id,branch_id,
    cost_code,crdd,brnd,contactless,booking)
select
        tran_id,
	tran_date,
	tran_creditor,
	tran_desc,
	tran_amount,
	cr_dr,
	tran_type_id,
	account_id,
	statement_date,
	cheque_no,
	receipt_ind,
	dd_ind,
	date_created,
	user_created,
	date_amended,
	user_amended,
	frequency,
	cred_id,
	branch_id,
	cost_code,
	crdd,
	brnd,
	contactless,
	booking
from transdet where tran_id=old.tran_id;
end */;;
DELIMITER ;

SELECT public.email_table.email
FROM public.email_table 
INNER JOIN public.data_table ON public.data_table.join_id=email_table.join_id
WHERE public.data_table.column_1%2=0 AND public.data_table.column_1>public.data_table.column_2 AND public.data_table.column_3%10=1;
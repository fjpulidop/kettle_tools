SELECT 
subscription_id, 
CASE WHEN sum(total_minutes) > 0 
	THEN true 
	ELSE false 
END AS is_active, 
'${DATE}' ::date AS "time" 
FROM staging.subscription_voice_by_day 
WHERE time::date BETWEEN ('${DATE}'::date - INTERVAL '30 day')::date AND '${DATE}' 
GROUP BY 1,3;


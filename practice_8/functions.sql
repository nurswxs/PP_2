CREATE OR REPLACE FUNCTION search_contacts(p text)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone
    FROM phonebook c
    WHERE c.name ILIKE '%' || p || '%'
       OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_contacts_paginated(limit_val INT, offset_val INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;

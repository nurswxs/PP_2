CREATE OR REPLACE PROCEDURE add_phone(p_contact_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO phones(contact_id, phone, type)
    SELECT id, p_phone, p_type FROM contacts WHERE name = p_contact_name;
END;
$$;


CREATE OR REPLACE PROCEDURE move_to_group(p_contact_name VARCHAR, p_group_name VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    g_id INTEGER;
BEGIN
    SELECT id INTO g_id FROM groups WHERE name = p_group_name;
    IF g_id IS NULL THEN
        INSERT INTO groups(name) VALUES (p_group_name) RETURNING id INTO g_id;
    END IF;
    UPDATE contacts SET group_id = g_id WHERE name = p_contact_name;
END;
$$;

CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(contact_name VARCHAR, email VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.email, p.phone
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.name ILIKE '%'||p_query||'%'
       OR c.email ILIKE '%'||p_query||'%'
       OR p.phone ILIKE '%'||p_query||'%';
END;
$$ LANGUAGE plpgsql;
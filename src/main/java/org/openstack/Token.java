package org.openstack;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Lob;
import lombok.Data;
import org.hibernate.annotations.GenericGenerator;

import java.util.Date;

@Data
@Entity
public class Token {

    @Id
    private String id;
    private Date expires;
    private String user;
    private String tenant;
    private String metadata;
    private String trustId;
    private String key;
    @Lob
    private String tokenData;
    private String userId;
    private String tokenVersion;

    public Token() {}
}

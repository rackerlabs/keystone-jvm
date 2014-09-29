package org.openstack;

import lombok.Data;

import java.util.Date;

@Data
public class Token {

    private String id;
    private Date expires;
    private String user;
    private String tenant;
    private String metadata;
    private String trustId;
    private String key;
    private String tokenData;
    private String userId;
    private String tokenVersion;

    public Token() {}
}

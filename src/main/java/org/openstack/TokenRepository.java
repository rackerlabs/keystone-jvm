package org.openstack;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

public interface TokenRepository extends CrudRepository<Token, Long> {

    List<Token> findByUser(String user);
}

package org.openstack;

import org.python.core.*;
import org.python.util.PythonInterpreter;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@EnableAutoConfiguration
@PropertySource("file:${config_dir:./etc}/app-config.properties")
public class Keystone {
    public static void main(String []args) throws PyException {
        PythonInterpreter pythonInterpreter = new PythonInterpreter();
        pythonInterpreter.exec("from keystone_jvm.common import wsgi; wsgi.run()");
    }
}

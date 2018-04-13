//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.4 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2018.04.11 at 05:58:01 PM PDT 
//


package com.microsoft.Malmo.Schemas;

import javax.xml.bind.annotation.XmlEnum;
import javax.xml.bind.annotation.XmlEnumValue;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for AbsoluteMovementCommand.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * <p>
 * <pre>
 * &lt;simpleType name="AbsoluteMovementCommand">
 *   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}string">
 *     &lt;enumeration value="tpx"/>
 *     &lt;enumeration value="tpy"/>
 *     &lt;enumeration value="tpz"/>
 *     &lt;enumeration value="tp"/>
 *     &lt;enumeration value="setYaw"/>
 *     &lt;enumeration value="setPitch"/>
 *   &lt;/restriction>
 * &lt;/simpleType>
 * </pre>
 * 
 */
@XmlType(name = "AbsoluteMovementCommand")
@XmlEnum
public enum AbsoluteMovementCommand {

    @XmlEnumValue("tpx")
    TPX("tpx"),
    @XmlEnumValue("tpy")
    TPY("tpy"),
    @XmlEnumValue("tpz")
    TPZ("tpz"),
    @XmlEnumValue("tp")
    TP("tp"),
    @XmlEnumValue("setYaw")
    SET_YAW("setYaw"),
    @XmlEnumValue("setPitch")
    SET_PITCH("setPitch");
    private final String value;

    AbsoluteMovementCommand(String v) {
        value = v;
    }

    public String value() {
        return value;
    }

    public static AbsoluteMovementCommand fromValue(String v) {
        for (AbsoluteMovementCommand c: AbsoluteMovementCommand.values()) {
            if (c.value.equals(v)) {
                return c;
            }
        }
        throw new IllegalArgumentException(v);
    }

}

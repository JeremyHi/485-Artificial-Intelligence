//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.4 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2018.04.11 at 05:58:01 PM PDT 
//


package com.microsoft.Malmo.Schemas;

import java.math.BigDecimal;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for anonymous complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;attribute name="timeLimitMs" use="required" type="{http://www.w3.org/2001/XMLSchema}decimal" />
 *       &lt;attribute name="description" type="{http://www.w3.org/2001/XMLSchema}string" default="" />
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "")
@XmlRootElement(name = "ServerQuitFromTimeUp")
public class ServerQuitFromTimeUp {

    @XmlAttribute(name = "timeLimitMs", required = true)
    protected BigDecimal timeLimitMs;
    @XmlAttribute(name = "description")
    protected String description;

    /**
     * Gets the value of the timeLimitMs property.
     * 
     * @return
     *     possible object is
     *     {@link BigDecimal }
     *     
     */
    public BigDecimal getTimeLimitMs() {
        return timeLimitMs;
    }

    /**
     * Sets the value of the timeLimitMs property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigDecimal }
     *     
     */
    public void setTimeLimitMs(BigDecimal value) {
        this.timeLimitMs = value;
    }

    /**
     * Gets the value of the description property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getDescription() {
        if (description == null) {
            return "";
        } else {
            return description;
        }
    }

    /**
     * Sets the value of the description property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setDescription(String value) {
        this.description = value;
    }

}

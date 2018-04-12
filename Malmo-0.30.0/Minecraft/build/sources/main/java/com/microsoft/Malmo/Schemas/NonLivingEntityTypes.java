//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.4 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2018.04.11 at 01:22:48 PM PDT 
//


package com.microsoft.Malmo.Schemas;

import javax.xml.bind.annotation.XmlEnum;
import javax.xml.bind.annotation.XmlEnumValue;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for NonLivingEntityTypes.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * <p>
 * <pre>
 * &lt;simpleType name="NonLivingEntityTypes">
 *   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}string">
 *     &lt;enumeration value="MinecartRideable"/>
 *     &lt;enumeration value="MinecartChest"/>
 *     &lt;enumeration value="MinecartFurnace"/>
 *     &lt;enumeration value="MinecartTNT"/>
 *     &lt;enumeration value="MinecartSpawner"/>
 *     &lt;enumeration value="MinecartHopper"/>
 *     &lt;enumeration value="MinecartCommandBlock"/>
 *     &lt;enumeration value="Boat"/>
 *     &lt;enumeration value="ArmorStand"/>
 *     &lt;enumeration value="ItemFrame"/>
 *     &lt;enumeration value="EnderCrystal"/>
 *     &lt;enumeration value="LeashKnot"/>
 *     &lt;enumeration value="Painting"/>
 *     &lt;enumeration value="PrimedTnt"/>
 *     &lt;enumeration value="FallingSand"/>
 *   &lt;/restriction>
 * &lt;/simpleType>
 * </pre>
 * 
 */
@XmlType(name = "NonLivingEntityTypes")
@XmlEnum
public enum NonLivingEntityTypes {

    @XmlEnumValue("MinecartRideable")
    MINECART_RIDEABLE("MinecartRideable"),
    @XmlEnumValue("MinecartChest")
    MINECART_CHEST("MinecartChest"),
    @XmlEnumValue("MinecartFurnace")
    MINECART_FURNACE("MinecartFurnace"),
    @XmlEnumValue("MinecartTNT")
    MINECART_TNT("MinecartTNT"),
    @XmlEnumValue("MinecartSpawner")
    MINECART_SPAWNER("MinecartSpawner"),
    @XmlEnumValue("MinecartHopper")
    MINECART_HOPPER("MinecartHopper"),
    @XmlEnumValue("MinecartCommandBlock")
    MINECART_COMMAND_BLOCK("MinecartCommandBlock"),
    @XmlEnumValue("Boat")
    BOAT("Boat"),
    @XmlEnumValue("ArmorStand")
    ARMOR_STAND("ArmorStand"),
    @XmlEnumValue("ItemFrame")
    ITEM_FRAME("ItemFrame"),
    @XmlEnumValue("EnderCrystal")
    ENDER_CRYSTAL("EnderCrystal"),
    @XmlEnumValue("LeashKnot")
    LEASH_KNOT("LeashKnot"),
    @XmlEnumValue("Painting")
    PAINTING("Painting"),
    @XmlEnumValue("PrimedTnt")
    PRIMED_TNT("PrimedTnt"),
    @XmlEnumValue("FallingSand")
    FALLING_SAND("FallingSand");
    private final String value;

    NonLivingEntityTypes(String v) {
        value = v;
    }

    public String value() {
        return value;
    }

    public static NonLivingEntityTypes fromValue(String v) {
        for (NonLivingEntityTypes c: NonLivingEntityTypes.values()) {
            if (c.value.equals(v)) {
                return c;
            }
        }
        throw new IllegalArgumentException(v);
    }

}

//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.4 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2018.04.11 at 05:58:01 PM PDT 
//


package com.microsoft.Malmo.Schemas;

import java.util.ArrayList;
import java.util.List;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlElements;
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
 *       &lt;group ref="{http://ProjectMalmo.microsoft.com}AgentMissionHandlers"/>
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "agentMissionHandlers"
})
@XmlRootElement(name = "AgentHandlers")
public class AgentHandlers {

    @XmlElements({
        @XmlElement(name = "ObservationFromRecentCommands", type = ObservationFromRecentCommands.class),
        @XmlElement(name = "ObservationFromHotBar", type = ObservationFromHotBar.class),
        @XmlElement(name = "ObservationFromFullStats", type = ObservationFromFullStats.class),
        @XmlElement(name = "ObservationFromFullInventory", type = ObservationFromFullInventory.class),
        @XmlElement(name = "ObservationFromSubgoalPositionList", type = ObservationFromSubgoalPositionList.class),
        @XmlElement(name = "ObservationFromGrid", type = ObservationFromGrid.class),
        @XmlElement(name = "ObservationFromDistance", type = ObservationFromDistance.class),
        @XmlElement(name = "ObservationFromDiscreteCell", type = ObservationFromDiscreteCell.class),
        @XmlElement(name = "ObservationFromChat", type = ObservationFromChat.class),
        @XmlElement(name = "ObservationFromNearbyEntities", type = ObservationFromNearbyEntities.class),
        @XmlElement(name = "ObservationFromRay", type = ObservationFromRay.class),
        @XmlElement(name = "ObservationFromTurnScheduler", type = ObservationFromTurnScheduler.class),
        @XmlElement(name = "VideoProducer", type = VideoProducer.class),
        @XmlElement(name = "RewardForTouchingBlockType", type = RewardForTouchingBlockType.class),
        @XmlElement(name = "RewardForSendingCommand", type = RewardForSendingCommand.class),
        @XmlElement(name = "RewardForSendingMatchingChatMessage", type = RewardForSendingMatchingChatMessage.class),
        @XmlElement(name = "RewardForCollectingItem", type = RewardForCollectingItem.class),
        @XmlElement(name = "RewardForDiscardingItem", type = RewardForDiscardingItem.class),
        @XmlElement(name = "RewardForReachingPosition", type = RewardForReachingPosition.class),
        @XmlElement(name = "RewardForMissionEnd", type = RewardForMissionEnd.class),
        @XmlElement(name = "RewardForStructureCopying", type = RewardForStructureCopying.class),
        @XmlElement(name = "RewardForTimeTaken", type = RewardForTimeTaken.class),
        @XmlElement(name = "RewardForCatchingMob", type = RewardForCatchingMob.class),
        @XmlElement(name = "RewardForDamagingEntity", type = RewardForDamagingEntity.class),
        @XmlElement(name = "ContinuousMovementCommands", type = ContinuousMovementCommands.class),
        @XmlElement(name = "AbsoluteMovementCommands", type = AbsoluteMovementCommands.class),
        @XmlElement(name = "DiscreteMovementCommands", type = DiscreteMovementCommands.class),
        @XmlElement(name = "InventoryCommands", type = InventoryCommands.class),
        @XmlElement(name = "ChatCommands", type = ChatCommands.class),
        @XmlElement(name = "SimpleCraftCommands", type = SimpleCraftCommands.class),
        @XmlElement(name = "MissionQuitCommands", type = MissionQuitCommands.class),
        @XmlElement(name = "TurnBasedCommands", type = TurnBasedCommands.class),
        @XmlElement(name = "AgentQuitFromTimeUp", type = AgentQuitFromTimeUp.class),
        @XmlElement(name = "AgentQuitFromReachingPosition", type = AgentQuitFromReachingPosition.class),
        @XmlElement(name = "AgentQuitFromTouchingBlockType", type = AgentQuitFromTouchingBlockType.class),
        @XmlElement(name = "AgentQuitFromCollectingItem", type = AgentQuitFromCollectingItem.class),
        @XmlElement(name = "AgentQuitFromReachingCommandQuota", type = AgentQuitFromReachingCommandQuota.class),
        @XmlElement(name = "AgentQuitFromCatchingMob", type = AgentQuitFromCatchingMob.class)
    })
    protected List<Object> agentMissionHandlers;

    /**
     * Gets the value of the agentMissionHandlers property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the agentMissionHandlers property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getAgentMissionHandlers().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link ObservationFromRecentCommands }
     * {@link ObservationFromHotBar }
     * {@link ObservationFromFullStats }
     * {@link ObservationFromFullInventory }
     * {@link ObservationFromSubgoalPositionList }
     * {@link ObservationFromGrid }
     * {@link ObservationFromDistance }
     * {@link ObservationFromDiscreteCell }
     * {@link ObservationFromChat }
     * {@link ObservationFromNearbyEntities }
     * {@link ObservationFromRay }
     * {@link ObservationFromTurnScheduler }
     * {@link VideoProducer }
     * {@link RewardForTouchingBlockType }
     * {@link RewardForSendingCommand }
     * {@link RewardForSendingMatchingChatMessage }
     * {@link RewardForCollectingItem }
     * {@link RewardForDiscardingItem }
     * {@link RewardForReachingPosition }
     * {@link RewardForMissionEnd }
     * {@link RewardForStructureCopying }
     * {@link RewardForTimeTaken }
     * {@link RewardForCatchingMob }
     * {@link RewardForDamagingEntity }
     * {@link ContinuousMovementCommands }
     * {@link AbsoluteMovementCommands }
     * {@link DiscreteMovementCommands }
     * {@link InventoryCommands }
     * {@link ChatCommands }
     * {@link SimpleCraftCommands }
     * {@link MissionQuitCommands }
     * {@link TurnBasedCommands }
     * {@link AgentQuitFromTimeUp }
     * {@link AgentQuitFromReachingPosition }
     * {@link AgentQuitFromTouchingBlockType }
     * {@link AgentQuitFromCollectingItem }
     * {@link AgentQuitFromReachingCommandQuota }
     * {@link AgentQuitFromCatchingMob }
     * 
     * 
     */
    public List<Object> getAgentMissionHandlers() {
        if (agentMissionHandlers == null) {
            agentMissionHandlers = new ArrayList<Object>();
        }
        return this.agentMissionHandlers;
    }

}

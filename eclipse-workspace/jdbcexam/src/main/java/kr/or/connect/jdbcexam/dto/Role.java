package kr.or.connect.jdbcexam.dto;

public class Role {
    
	// 단축키 alt + shift + s 
	
	private Integer roleId;
	private String description;
	public Integer getRoleId() {
		return roleId;
	}
	public void setRoleId(Integer roleId) {
		this.roleId = roleId;
	}
	public String getDescription() {
		return description;
	}
	public void setDescription(String description) {
		this.description = description;
	}
	
	@Override
	public String toString() {
		return "Role [roleId=" + roleId + ", description=" + description + "]";
	}
	
	
}

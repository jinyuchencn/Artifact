#version 330 core
out vec4 FragColor;

struct Material {
    sampler2D diffuse;
    sampler2D specular;    
    float shininess;
}; 

struct Light {
    vec3 position;

	vec3 direction;
    float cutOff;
    float outerCutOff;

    vec3 ambient;
    vec3 diffuse;
    vec3 specular;

	float constant;
    float linear;
    float quadratic;


};


struct FogInfo {
  float maxDist;
  float minDist;
  vec3 color;
};
uniform FogInfo Fog;
uniform float timeFogFactor;


in vec3 FragPos;  
in vec3 Normal;  
in vec2 TexCoords;
  
uniform vec3 viewPos;
uniform Material material;
uniform Light light;
uniform vec3 flashLightOpen;

void main()
{
	//fog
	float dist = abs( (FragPos.x - viewPos.x) * (FragPos.x - viewPos.x ) + ( FragPos.y - viewPos.y ) * ( FragPos.y - viewPos.y ) + ( FragPos.z - viewPos.z ) * ( FragPos.z - viewPos.z ));
	float disFogFactor = dist/ (Fog.maxDist - Fog.minDist);
    disFogFactor = clamp( disFogFactor, 0.0, 1.0 );

	float fogFactor = timeFogFactor*disFogFactor;

	fogFactor = clamp( fogFactor, 0.0, 1.0 );
	// lightDir


    vec3 lightDir = normalize(light.position - FragPos);
    
    // check if lighting is inside the spotlight cone
    float theta = dot(lightDir, normalize(-light.direction)); 


	
	
	if(theta > light.cutOff) // remember that we're working with angles as cosines instead of degrees so a '>' is used.
    {  
		// ambient
		vec3 ambient = light.ambient * texture(material.diffuse, TexCoords).rgb;
  	
		// diffuse 
		vec3 norm = normalize(Normal);  
		float diff = abs(dot(norm, lightDir));
		vec3 diffuse = light.diffuse * diff * texture(material.diffuse, TexCoords).rgb;  
    
		// specular
		vec3 viewDir = normalize(viewPos - FragPos);
		vec3 reflectDir = reflect(-lightDir, norm);  
		float spec = pow(abs(dot(viewDir, reflectDir)), material.shininess);
		vec3 specular = light.specular * spec * texture(material.specular, TexCoords).rgb;  
		// attenuation
        float distance    = length(light.position - FragPos);
        float attenuation = 1.0 / (light.constant + light.linear * distance + light.quadratic * (distance * distance));  

		diffuse   *= attenuation;
        specular *= attenuation; 
        
		vec3 result = ambient + diffuse * flashLightOpen + specular * flashLightOpen;
		
		vec3 color = mix(result , Fog.color, fogFactor );
		//vec3 result = ambient + diffuse * vec3(1.0,1.0,1.0) + specular*vec3(1.0,1.0,1.0) ;
		FragColor = vec4(color, 1.0);
	}
	    else 
    {
        // else, use ambient light so scene isn't completely dark outside the spotlight.
		vec3 result =light.ambient * texture(material.diffuse, TexCoords).rgb;
		vec3 color = mix(result , Fog.color, fogFactor );

		FragColor = vec4(color, 1.0);
    }
} 
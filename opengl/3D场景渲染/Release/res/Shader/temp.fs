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

in vec3 FragPos;
in vec3 Normal;
in vec2 TexCoords;

uniform vec3 viewPos;
uniform Material material;
uniform Light light;
uniform vec3 reconColor;
uniform vec3 flashLightOpen;

void main()
{
    vec3 lightDir = normalize(light.position - FragPos);

    // check if lighting is inside the spotlight cone
    float theta = dot(lightDir, normalize(-light.direction));
    vec3 color = reconColor;
	if(theta > light.cutOff) // remember that we're working with angles as cosines instead of degrees so a '>' is used.
    {
		// ambient

        vec3 ambient = light.ambient * color;

		// diffuse
		vec3 norm = normalize(Normal);
		float diff = abs(dot(norm, lightDir));
        
		vec3 diffuse = light.diffuse * diff * color;

		// specular
		vec3 viewDir = normalize(viewPos - FragPos);
		vec3 reflectDir = reflect(-lightDir, norm);
		float spec = pow(abs(dot(viewDir, reflectDir)), material.shininess);
		vec3 specular = light.specular * spec * color;
		// attenuation
        float distance    = length(light.position - FragPos);
        float attenuation = 1.0 / (light.constant + light.linear * distance + light.quadratic * (distance * distance));

		diffuse   *= attenuation;
        specular *= attenuation;

		vec3 result = ambient + diffuse * flashLightOpen + specular * flashLightOpen ;
		FragColor = vec4(result, 1.0);
	}
	    else
    {
        // else, use ambient light so scene isn't completely dark outside the spotlight.
        FragColor = vec4(light.ambient * color, 1.0);
    }
}

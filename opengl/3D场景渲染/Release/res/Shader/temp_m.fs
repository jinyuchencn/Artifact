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

void main()
{
	//fog
	float dist = abs( (FragPos.x - viewPos.x) * (FragPos.x - viewPos.x ) + ( FragPos.y - viewPos.y ) * ( FragPos.y - viewPos.y ) + ( FragPos.z - viewPos.z ) * ( FragPos.z - viewPos.z ));
	float disFogFactor = dist/ (Fog.maxDist - Fog.minDist);
    disFogFactor = clamp( disFogFactor, 0.0, 1.0 );

	float fogFactor = timeFogFactor*disFogFactor;

	fogFactor = clamp( fogFactor, 0.0, 1.0 );
    // ambient 环境光
    vec3 ambient = light.ambient * texture(material.diffuse, TexCoords).rgb;

    // diffuse 漫反射
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(light.position - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = light.diffuse * diff * texture(material.diffuse, TexCoords).rgb;

    // specular 镜面反射
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), material.shininess);
    vec3 specular = light.specular * spec * texture(material.specular, TexCoords).rgb;

    vec3 result = ambient + diffuse + specular;

    vec3 color = mix(result , Fog.color, fogFactor );
	FragColor = vec4(color, 1.0);
}

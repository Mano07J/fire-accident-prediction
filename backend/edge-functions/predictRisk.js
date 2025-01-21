import { createClient } from '@supabase/supabase-js';

const supabaseUrl = Deno.env.get('SUPABASE_URL');
const supabaseKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY');
const supabase = createClient(supabaseUrl, supabaseKey);

export default async (req) => {
  const { temperature, smoke, humidity, gas } = req.body;
  const fire_risk = temperature > 70 || smoke > 0.5 || gas > 0.5;

  const { data, error } = await supabase.from('sensor_data').insert({
    temperature,
    smoke,
    humidity,
    gas,
    fire_risk,
  });

  return new Response(JSON.stringify({ success: !error, fire_risk }));
};
